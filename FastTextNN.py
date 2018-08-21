import pexpect

FASTTEXT_PATH = "fasttext"
NUM_NEIGHBORS = 10

class NNLookup:
    """Class for using the command-line interface to fasttext nn to lookup neighbours.
    It's rather fiddly and depends on exact text strings. But it is at least short and simple."""
    def __init__(self, model_path):
        self.nn_process = pexpect.spawn('%s nn %s %d' % (FASTTEXT_PATH, model_path, NUM_NEIGHBORS))
        self.nn_process.expect('Query word?')  # Flush the first prompt out.

    def get_nn(self, word):
        self.nn_process.sendline(word)
        self.nn_process.expect('Query word?')
        output = self.nn_process.before
        output = output.decode("utf-8")
        result = [{"key":line.strip().split()[0],"value":line.strip().split()[1]} for line in output.strip().split('\n')[1:]]
        return result