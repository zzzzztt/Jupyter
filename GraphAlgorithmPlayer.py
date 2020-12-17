import valueplayerwidget
from GraphAlgorithmView import GraphAlgorithmView


class GraphAlgorithmPlayer(valueplayerwidget.ValuePlayerWidget):
    """
        A ValuePlayerWidget for graphs
    """
    def __init__(self, graph, variables=[], view='networkx', nodeLabels=None, edgeLabels=None):
        """
            Initialization
            
            Parameters
            ---------
            graph : the graph to display
            variables : defines the local variables we are interested in
            view : defines wether to use Networkx or BQPlot to display the graph
            nodeLabels : Labels for nodes
            edgeLabels : Labels for edges
            
        """
        self.__view = GraphAlgorithmView(graph, variables=variables, view=view, nodeLabels=nodeLabels, edgeLabels=edgeLabels)
        valueplayerwidget.ValuePlayerWidget.__init__(self,self.__view)
    
    def newGraph(self, graph):
        """
            Display a new graph
        """
        self.player.reset(dict())
        self.__view.newGraph(graph)