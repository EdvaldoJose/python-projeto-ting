from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    mock = [
        {'qtd_linhas': 7}, {'qtd_linhas': 6}, {'qtd_linhas': 1},
        {'qtd_linhas': 2}, {'qtd_linhas': 3},
    ]

    sp_queue = PriorityQueue()

    sp_queue.enqueue(mock[1])
    sp_queue.enqueue(mock[2])
    sp_queue.enqueue(mock[3])
    sp_queue.enqueue(mock[4])
    sp_queue.enqueue(mock[0])

    assert len(sp_queue) == 5
    assert sp_queue.search(2) == mock[4]
    assert sp_queue.search(3) == mock[1]

    with pytest.raises(IndexError):
        sp_queue.search(10)

    assert sp_queue.dequeue() == mock[2]
    assert sp_queue.dequeue() == mock[3]
    assert sp_queue.dequeue() == mock[4]
    assert sp_queue.dequeue() == mock[1]
    assert sp_queue.dequeue() == mock[0]

    assert len(sp_queue) == 0

    sp_queue.enqueue(mock[0])
    sp_queue.enqueue(mock[1])

    assert len(sp_queue) == 2
