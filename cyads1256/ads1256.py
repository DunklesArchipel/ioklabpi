from lowlevel import ads_init, read_and_set_next_channel

class ADS1256:
    def __init__(self, datarate, buffered=False, gain=1):
        if buffered:
            raise NotImplementedError

        self.next_channel = -1
        self.next_timestamp = None
        self.gain = gain

        ads_init(datarate, gain)

    def read(self, channels, final_next_channel=None):
        ret = []
        if final_next_channel is None:
            final_next_channel = channels[0]
        for (channel, next_channel) in zip(channels,channels[1:]+[final_next_channel]):
            if channel != self.next_channel:
                if self.next_channel != -1:
                    # TODO: log a warning if this is not the initial call
                    raise Exception
                self._read_and_set_next_channel(next_channel)
            timestamp, raw = self._read_and_set_next_channel(next_channel)
            ret.append((timestamp, raw/1.67e6/self.gain))
        return ret

    def _read_and_set_next_channel(self, next_channel):
        from time import time
        # WARNING: against pin 3
        ret = self.next_timestamp, read_and_set_next_channel((next_channel << 4) | 3)
        # ret = self.next_timestamp, read_and_set_next_channel((next_channel << 4) | (1<<3))
        self.next_channel = next_channel
        self.next_timestamp = time()
        return ret

    def _read_previous_channel(self):
        raise NotImplementedError
