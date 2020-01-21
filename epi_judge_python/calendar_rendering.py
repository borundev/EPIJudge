import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint=collections.namedtuple('Endpoint',('time','is_start'))

def find_max_simultaneous_events(A: List[Event]) -> int:

    # For each event make two endpoints with flag for start/end
    eps= [p for event in A for p in (Endpoint(event.start,True),Endpoint(event.finish,False))]

    # Sort the endpoints with tie breaker being start_time < end_time
    # not e.is_start means start will be False and thus 0 and finish will be True and so 1
    # this will ensure that start comes before finish
    eps.sort(key=lambda e: (e.time,not e.is_start))

    max_simultaneous_events, simultaneous_events=0,0

    for e in eps:
        if e.is_start:
            simultaneous_events+=1
            max_simultaneous_events=max(max_simultaneous_events,simultaneous_events)
        else:
            simultaneous_events-=1

    return max_simultaneous_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
