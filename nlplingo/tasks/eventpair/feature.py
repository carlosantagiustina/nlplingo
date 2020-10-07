

# +1
class EventPairFeature(object):
    def __init__(self, features):
        """
        :type features: list[str]
        """
        self.feature_strings = features

        self.c_trigger_window_vector1 = 'trigger_window_vector1'
        self.c_trigger_window_vector2 = 'trigger_window_vector2'

        self.trigger_window_vector1 = self.c_trigger_window_vector1 in features
        self.trigger_window_vector2 = self.c_trigger_window_vector2 in features


# +1
# This class is very simple because it does not actually generate features itself.
# Instead, it simply uses the features generated by the trigger model. Currently, to represent a pair of event mentions,
# it uses just the embeddings associated with the two anchors (with optional window size)
class EventPairFeatureGenerator(object):
    def __init__(self, params):
        self.features = EventPairFeature(params['features'])
        """:type nlplingo.tasks.eventpair.feature.EventPairFeature"""


