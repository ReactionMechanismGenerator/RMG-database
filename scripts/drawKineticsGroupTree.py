#!/usr/bin/env python
# encoding: utf-8

"""
This script draws the group tree for the specified kinetics family,
including diagrams for each group definition.

Optionally, a second argument can be provided to indicate a head node
to start at. If specified, the output will only include the specified
node and its children.

Saves output as a pdf.
"""

import os
import argparse
import pydot
import rmgpy
from collections import OrderedDict

from rmgpy.data.kinetics import KineticsDatabase
from rmgpy.molecule import Group


def convert(family, top_node=None):

    database_path = rmgpy.settings['database.directory']
    family_path = os.path.join(database_path, 'kinetics', 'families')

    kinetics = KineticsDatabase()
    kinetics.loadFamilies(family_path, families=[family])

    if top_node is not None:
        selected_entries = OrderedDict()
        selected_entries[top_node] = kinetics.families[family].groups.entries[top_node]
        queue = [selected_entries[top_node]]
        for item in queue:
            if item.children:
                queue.extend(item.children)
                for child in item.children:
                    selected_entries[child.label] = child
    else:
        selected_entries = kinetics.families[family].groups.entries

    groups = []
    graph = pydot.Dot(graph_type='graph', dpi='52')
    for label, entry in selected_entries.iteritems():
        if entry.index == -1:
            continue
        elif isinstance(entry.item, Group):
            image_path = draw_group(label, entry.item)
            node_label = '<<TABLE border="0">\n<TR><TD>{1}</TD></TR>\n<TR><TD><IMG scale="True" SRC="{0}"/></TD></TR>\n</TABLE>>'.format(os.path.join(image_path), label)
        else:
            node_label = str(entry.item)
            node_label = '"' + label + '\n' + node_label + '"'

        groups.append(label)
        index1 = groups.index(label) + 1
        graph.add_node(pydot.Node(name=str(index1), label=node_label, fontname="Helvetica", fontsize="16", shape="box"))
        if entry.label != top_node and entry.parent is not None:
            index2 = groups.index(entry.parent.label) + 1
            graph.add_edge(pydot.Edge(src=str(index2), dst=str(index1), fontname="Helvetica", fontsize="16"))

    outputPath = family + '_groups.pdf'
    graph.write_pdf(outputPath, prog='dot')


def draw_group(label, group):

    label = label.replace('/', '_')
    path = os.path.join(os.getcwd(), 'images', label + '.png')

    if os.path.exists(path):
        return path
    elif not os.path.exists('images'):
        os.makedirs('images')

    with open(path, 'w') as f:
        f.write(group.draw('png'))

    return path


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('family', metavar='FAMILY', type=str, nargs=1,
                        help='The name of the kinetics family')
    parser.add_argument('head', metavar='HEAD', type=str, nargs='?', default=None,
                        help='The top node to start at')

    args = parser.parse_args()
    family = args.family[0]
    head = args.head[0]

    convert(family, head)
