from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        #test case for joy
        emotion1 = emotion_detector("I am glad this happened")
        # print(emotion1)
        self.assertEqual(emotion1['dominant_emotion'], 'joy')
        #test case for anger
        emotion2 = emotion_detector("I am really mad about this")
        self.assertEqual(emotion2['dominant_emotion'], 'anger')
        #test case for disgust
        emotion3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(emotion3['dominant_emotion'], 'disgust')
        #test case for sadness
        emotion4 = emotion_detector("I am so sad about this")
        self.assertEqual(emotion4['dominant_emotion'], 'sadness')
        #test case for fear
        emotion5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(emotion5['dominant_emotion'], 'fear')

unittest.main()