#this belongs in apps/methods/ svg_shared_icons.py - Version: 1
# X-Seti - Nov21 2025 - IMG Factory 1.5 - SVG Icon Management System
"""
SVG Icon Management System - Provides shared SVG icons for IMG Factory GUI components.
"""

##Methods list -
# get_add_icon
# get_checkmark_icon
# get_close_icon
# get_edit_icon
# get_open_icon
# get_refresh_icon
# get_remove_icon
# get_search_icon
# get_export_icon
# get_import_icon
# get_save_icon
# get_delete_icon
# get_settings_icon
# get_trash_icon
# get_view_icon

import base64

def get_close_icon(): #vers 1
    """
    Returns SVG data for close icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMTIgNGwtNCA0LTQtNGwtMiAyIDQgNCA0LTR6Ii8+PC9zdmc+"""
    return base64.b64decode(svg_data).decode('utf-8')


def get_remove_icon(): #vers 1
    """
    Returns SVG data for remove icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMTQgNWwtNSA1LTUtNWwtMiAyIDcgNyA3LTd6Ii8+PC9zdmc+"""
    return base64.b64decode(svg_data).decode('utf-8')


def get_add_icon(): #vers 1
    """
    Returns SVG data for add icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMTQgN2gtN1YySDV2NUgxdjJoNGw1IDV2LTloN1Y3eiIvPjwvc3ZnPg=="""
    return base64.b64decode(svg_data).decode('utf-8')

def get_edit_icon(): #vers 1
    """
    Returns SVG data for edit icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMTQuMjggMi43MmMtLjI4LS4yOC0uNzMtLjI4LTEuMDIgMEw5LjUgNi41IDExIDhMMTUgNC4yOHptLTIuODUgMi44NUw1LjUgMTEuNWwtMyAzTDMgMTNsMy0zLjkzaDMuODN6Ii8+PC9zdmc+"""
    return base64.b64decode(svg_data).decode('utf-8')

def get_open_icon(): #vers 1
    """
    Returns SVG data for open icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNNCAyaDh2Mkg0VjJ6bTAtNGg4YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJINEMyLjkgMiAyIDIuOSAyIDR2MTJjMCAxLjEuOSAyIDIgMmg4YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJINiIvPjwvc3ZnPg=="""
    return base64.b64decode(svg_data).decode('utf-8')

def get_refresh_icon(): #vers 1
    """
    Returns SVG data for refresh icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMTQgN2gtMlY1YzAtLjU1LS40NS0xLTEtMUg1Yy0uNTUgMC0xIC40NS0xIDF2NGMwIC41NS40NSAxIDEgMWg0djJoLTNjLS41NSAwLTEgLjQ1LTEgMVYxNGMwIC41NS40NSAxIDEgMWg0Yy41NSAwIDEtLjQ1IDEtMVY4YzAtLjU1LS40NS0xLTEtMXoiLz48L3N2Zz4="""
    return base64.b64decode(svg_data).decode('utf-8')

def get_search_icon(): #vers 1
    """
    Returns SVG data for search icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMTUuNzEgMTQuMjlsLTMuOTMtMy45M2MtLjUzLjQ1LTEuMjMuNzEtMi4wMS43MS0xLjc3IDAtMy4yLTEuNDMtMy4yLTNzMS40My0zLjIgMy4yLTMuMmMxLjc3IDAgMy4yIDEuNDMgMy4yIDNzLTEuNDMgMy4yLTMuMiAzLjJjLjc4IDAgMS40OC0uMjYgMi4wMS0uNzFsMy45MyAzLjkzYy4zOS4zOS4zOSAxLjA0IDAgMS40MS0uMTkuMTktLjQ1LjI5LS43MS4yOS0uMjYgMC0uNTItLjEtLjcxLS4yOXptLTcuNzEgMGgtMlY5aDJ2NVoiLz48L3N2Zz4="""
    return base64.b64decode(svg_data).decode('utf-8')

def get_export_icon(): #vers 1
    """
    Returns SVG data for export icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMTQgMTB2Mkg2VjhoNGwtNCA0IDQgNGwtNCA0djJoMTBWNHoiLz48L3N2Zz4="""
    return base64.b64decode(svg_data).decode('utf-8')

def get_import_icon(): #vers 1
    """
    Returns SVG data for import icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMiAxMHYySDh2NGwyLTQgMiA0LTIgNGg0djJoLTEwVjRIMlYxMHptMTIgMmwtNCA0djJoMTB2Mmg0VjRoLTEweiIvPjwvc3ZnPg=="""
    return base64.b64decode(svg_data).decode('utf-8')

def get_save_icon(): #vers 1
    """
    Returns SVG data for save icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMTQgMmgxVjBoLTF2Mkg2VjBoLTF2MkgxdjE0aDE0VjJoLTV2Mmgzdi0zemgtOVY3aDlWNWgtM3Yzemg3VjJoM3YxMkgxdjJoMTRWNHoiLz48L3N2Zz4="""
    return base64.b64decode(svg_data).decode('utf-8')

def get_delete_icon(): #vers 1
    """
    Returns SVG data for delete icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMSA0aDE0djJIMFY0em0xMiA3aC0yVjZoMnY1em0tNCAwaC0yVjZoMnY1em0tNCAwaC0yVjZoMnY1ek00IDRIMFYyaDR2MnoiLz48L3N2Zz4="""
    return base64.b64decode(svg_data).decode('utf-8')

def get_settings_icon(): #vers 1
    """
    Returns SVG data for settings icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMTIuMzcgMTIuM2MtLjQzLjI4LTEuMDMuMjgtMS40NiAwbC0uNjMtLjQxLS42My40MWMtLjQzLjI4LTEuMDMuMjgtMS40NiAwbC0uNDMtLjYzbC0uNjMuNDFjLS40My4yOC0xLjAzLjI4LTEuNDYgMGwtLjQzLS42M2wuNjMtLjQxYy40My0uMjguNDMtLjg4IDAtMS4xNmwtLjYzLS40M2wuNDMtLjYzYy4yOC0uNDMuMjgtMS4wMyAwLTEuNDZsLjYzLS40M2wtLjYzLS40M2MtLjI4LS40My0uMjgtMS4wMyAwLTEuNDZsLjYzLS40M2wuNjMuNDFjLjQzLjI4IDEuMDMuMjggMS40NiAwbC40My0uNjNsLjYzLjQxYy40My4yOCAxLjAzLjI4IDEuNDYgMGwuNDMtLjYzbC42My40MWMuNDMuMjguNDMuODggMCAxLjE2bC0uNjMuNDRsLS40My0uNjNjLS4yOC0uNDMtLjI4LTEuMDMgMC0xLjQ2bC42My0uNDNsLS42My0uNDRjLS40My0uMjgtMS4wMy0uMjgtMS40NiAwbC0uNDMuNjNsLS42My0uNDFjLS40My0uMjgtMS4wMy0uMjgtMS40NiAwbC0uNDMtLjYzbC42My0uNDFjLjQzLS4yOCAxLjAzLS4yOCAxLjQ2IDBsLjQzLjYzbC42My0uNDFjLjQzLS4yOCAxLjAzLS4yOCAxLjQ2IDBsLjQzLjYzLS42My40MWMtLjQzLjI4LS40My44OCAwIDEuMTZsLjYzLjQzLS40My42M2MtLjI4LjQzLS4yOCAxLjAzIDAgMS40NmwtLjYzLjQzbC42My40MWMuNDMuMjguNDMuODggMCAxLjE2eiIvPjwvc3ZnPg=="""
    return base64.b64decode(svg_data).decode('utf-8')


def get_trash_icon(): #vers 1
    """
    Returns SVG data for trash icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMSA0aDE0djJIMFY0em0xMiA3aC0yVjZoMnY1em0tNCAwaC0yVjZoMnY1em0tNCAwaC0yVjZoMnY1ek00IDRIMFYyaDR2MnoiLz48L3N2Zz4="""
    return base64.b64decode(svg_data).decode('utf-8')


def get_view_icon(): #vers 1
    """
    Returns SVG data for view icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMSA4YzIuMjEgMCA0LTQgOC00czYgNCA4IDRzLTIuNzkgNC04IDRjLTIuMjEgMC00LTQtOC00em0wLjUgMGMxLjY2IDAgMy4zMi0xLjQ4IDQuNS0zLjUtMS4xOCAyLjAyLTIuODQgMy41LTQuNSAzLjV6bTcuNSA0YzIuMjEgMCA0LTQgOC00czYgNCA4IDRzLTIuNzkgNC04IDRjLTIuMjEgMC00LTQtOC00eiIvPjwvc3ZnPg=="""
    return base64.b64decode(svg_data).decode('utf-8')


def get_checkmark_icon(): #vers 1
    """
    Returns SVG data for checkmark icon as base64 string
    """
    svg_data = """PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMTQgNGwtNiA2LTQtNHoiLz48L3N2Zz4="""
    return base64.b64decode(svg_data).decode('utf-8')
