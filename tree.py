import streamlit as st
import graphviz

def show_decision_tree():
    # Create a decision tree structure using Graphviz
    dot = graphviz.Digraph(comment='Decision Tree for Restaurant Location')

    # Add nodes and edges with colors to represent the decision tree
    dot.node('A', 'Population Density', shape='ellipse')
    dot.node('B', 'High', shape='box', style='filled', fillcolor='lightgreen')  # Success
    dot.node('C', 'Low', shape='box', style='filled', fillcolor='lightcoral')   # Low Success
    dot.node('D', 'Competitor Density', shape='ellipse')
    dot.node('E', 'Low', shape='box', style='filled', fillcolor='lightcoral')   # Low Success
    dot.node('F', 'High', shape='box', style='filled', fillcolor='lightgreen')   # Success
    dot.node('G', 'Market Trend', shape='ellipse')
    dot.node('H', 'Favorable', shape='box', style='filled', fillcolor='lightgreen')  # Success
    dot.node('I', 'Unfavorable', shape='box', style='filled', fillcolor='lightcoral') # Low Success
    dot.node('J', 'Accessibility', shape='ellipse')
    dot.node('K', 'Good', shape='box', style='filled', fillcolor='lightgreen')      # Success
    dot.node('L', 'Low Success', shape='box', style='filled', fillcolor='lightcoral') # Low Success
    dot.node('M', 'High Success', shape='box', style='filled', fillcolor='lightgreen') # Success

    # Connect the nodes with edges
    dot.edges(['AB', 'AC', 'BD', 'BF', 'DG', 'GH', 'GI', 'HJ', 'JK', 'JL'])
    dot.edge('B', 'D', label='High')
    dot.edge('D', 'E', label='Low')
    dot.edge('D', 'F', label='High')
    dot.edge('H', 'J', label='Favorable')
    dot.edge('I', 'L', label='Unfavorable')
    dot.edge('J', 'K', label='Good')
    dot.edge('K', 'M', label='High Success')
    dot.edge('K', 'L', label='Low Success')

    # Render the decision tree as a graph
    st.graphviz_chart(dot)

# Streamlit application
def main():
    st.title("Restaurant Location Decision Tree")
    st.write("This decision tree helps evaluate the probability of success when opening a new restaurant.")
    show_decision_tree()

if __name__ == "__main__":
    main()
