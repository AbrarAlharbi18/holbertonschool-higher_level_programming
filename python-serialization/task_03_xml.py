#!/usr/bin/env python3
"""
Module to serialize and deserialize dictionaries using XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to an XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Output XML file name.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except Exception:
        pass


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a dictionary.

    Args:
        filename (str): XML file name to read from.

    Returns:
        dict: Dictionary reconstructed from XML data.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for element in root:
            result[element.tag] = element.text

        return result
    except Exception:
        return None
