import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.begin = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        delta = self.end - self.begin
        print(f"time: {delta}")


@contextmanager
def cm_timer_2():
    begin = time.time()
    yield
    delta = time.time() - begin
    print(f"time: {delta}")


if __name__ == "__main__":
    with cm_timer_1():  # time: 5.505076169967651
        time.sleep(5.5)

    with cm_timer_2():  # time: 5.504739761352539
        time.sleep(5.5)
