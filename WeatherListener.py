from Lego import Lego
import Message
import threading


class WeatherListener(Lego):
    class ZipCodeListener(Lego):
        def listening_for(self, message):
            return '90210' in message['text']

        def handle(self, message):
            metadata = {"source": self, "dest": message['metadata']['source']}
            response = {"text": "The weather is sunny!", "metadata": metadata}
            self.baseplate.tell(response)
            self.finished = True
            self.actor_ref.stop()

        def on_stop(self):
            print('ZipCodeListener stopped')

        def on_failure(self, exception_type, exception_value, traceback):
            print('ZipCodeListener crashed')

    def listening_for(self, message):
        return '!weather' in message['text']

    def handle(self, message):
        metadata = {"source": self}
        response = {"text": "Please enter a zipcode.", "metadata": metadata}
        self.baseplate.tell(response)
        lock = threading.Lock()
        lock.acquire()
        self.children.append(self.ZipCodeListener.start(self.baseplate))
        print(self.children)
        lock.release()

    def on_failure(self, exception_type, exception_value, traceback):
        print('WeatherListener crashed.')
        print(exception_type)
        print(exception_value)
