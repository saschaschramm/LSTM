from Basics.lstm_with_cell import Model
import unittest

class TestLSTM(unittest.TestCase):

    def test_lstm_with_cell(self):
        x0 = [[1.0, 2.0]]
        x1 = [[0.5, 3.0]]
        inputs = [x0, x1]

        label0 = [[0.5]]
        label1 = [[1.25]]
        labels = [label0, label1]

        model = Model()
        for i in range(0, 2):
            loss = model.train(inputs, labels)
            print("loss", loss)

        self.assertAlmostEqual(loss[0][0], 1.4493194)

if __name__ == '__main__':
    unittest.main()