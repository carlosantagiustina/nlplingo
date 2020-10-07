
class EventFramePairFeature(object):
    def __init__(self, features):
        """
        :type features: list[str]
        """
        self.feature_strings = features

        self.c_trigger_window_vector1 = 'trigger_window_vector1'
        self.c_trigger_window_vector2 = 'trigger_window_vector2'

        self.c_agent_window_vector1 = 'agent_window_vector1'
        self.c_agent_window_vector2 = 'agent_window_vector2'

        self.c_patient_window_vector1 = 'patient_window_vector1'
        self.c_patient_window_vector2 = 'patient_window_vector2'

        self.trigger_window_vector1 = self.c_trigger_window_vector1 in features
        self.trigger_window_vector2 = self.c_trigger_window_vector2 in features

        self.agent_window_vector1 = self.c_agent_window_vector1 in features
        self.agent_window_vector2 = self.c_agent_window_vector2 in features

        self.patient_window_vector1 = self.c_patient_window_vector1 in features
        self.patient_window_vector2 = self.c_patient_window_vector2 in features


# This class is very simple because it does not actually generate features itself.
# Instead, it simply uses the features generated by the trigger and argument.
class EventFramePairFeatureGenerator(object):
    def __init__(self, params):
        self.features = EventFramePairFeature(params['features'])
        """:type nlplingo.tasks.eventframe.feature.EventFramePairFeature"""
