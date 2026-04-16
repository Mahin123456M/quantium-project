import pytest
from dash.testing.application_runners import import_app


app = import_app('app')

def test_header_present():
    """Test that the header is present in the app layout"""

    layout = app.layout

    # Check that there's an H1 element with the correct text
    h1_elements = []
    def find_h1_elements(component):
        if hasattr(component, 'children'):
            if isinstance(component.children, list):
                for child in component.children:
                    find_h1_elements(child)
            else:
                if hasattr(component, 'children') and str(component.children) == "Pink Morsel Sales Analysis":
                    h1_elements.append(component)
        elif hasattr(component, 'props') and 'children' in component.props:
            if component.props['children'] == "Pink Morsel Sales Analysis":
                h1_elements.append(component)

    find_h1_elements(layout)

    
    assert len(h1_elements) > 0

def test_visualisation_present():
    """Test that the visualisation chart is present in the app layout"""
    layout = app.layout

    # Check that there's a Graph component with id 'sales-chart'
    graph_found = False
    def find_graph(component):
        nonlocal graph_found
        if hasattr(component, 'id') and component.id == 'sales-chart':
            graph_found = True
        if hasattr(component, 'children'):
            if isinstance(component.children, list):
                for child in component.children:
                    find_graph(child)
            else:
                find_graph(component.children)

    find_graph(layout)

    assert graph_found, "Graph component with id 'sales-chart' not found"

def test_region_picker_present():
    """Test that the region picker radio buttons are present in the app layout"""
    layout = app.layout

    
    radio_found = False
    def find_radio(component):
        nonlocal radio_found
        if hasattr(component, 'id') and component.id == 'region-radio':
            radio_found = True
        if hasattr(component, 'children'):
            if isinstance(component.children, list):
                for child in component.children:
                    find_radio(child)
            else:
                find_radio(component.children)

    find_radio(layout)

    assert radio_found, "RadioItems component with id 'region-radio' not found"

    
    radio_options = []
    def find_radio_options(component):
        if hasattr(component, 'id') and component.id == 'region-radio':
            if hasattr(component, 'options'):
                radio_options.extend(component.options)
        if hasattr(component, 'children'):
            if isinstance(component.children, list):
                for child in component.children:
                    find_radio_options(child)
            else:
                find_radio_options(component.children)

    find_radio_options(layout)

    
    expected_labels = ['All Regions', 'North', 'East', 'South', 'West']
    actual_labels = [opt['label'] for opt in radio_options] if radio_options else []

    assert len(actual_labels) == 5, f"Expected 5 radio options, got {len(actual_labels)}"
    assert set(actual_labels) == set(expected_labels), f"Radio options don't match. Expected {expected_labels}, got {actual_labels}"