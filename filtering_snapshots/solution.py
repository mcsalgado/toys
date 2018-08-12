#!/usr/bin/env python3

from datetime import datetime, timedelta
from collections import defaultdict

example_input = [
    ('butt-1', datetime(2016, 10, 1, 13, 8, 29), 'available'),
    ('butt-2', datetime(2017, 1, 20, 17, 1, 33), 'available'),
    ('butt-3', datetime(2017, 1, 22, 7, 43, 21), 'pending'),
    ('butt-1-feet', datetime(2017, 1, 17, 11, 41, 36), 'available'),
    ('lol-1-feet', datetime(2016, 10, 15, 2, 55, 31), 'available'),
    ('lol-2-feet', datetime(2016, 12, 11, 9, 22, 33), 'available'),
    ('lol-scene-1', datetime(2016, 10, 1, 10, 8, 28), 'available'),
    ('lol-scene-2', datetime(2016, 10, 16, 10, 9, 24), 'available'),
    ('lol-scene-3', datetime(2016, 11, 1, 10, 7, 43), 'available'),
    ('lol-scene-4', datetime(2016, 11, 16, 10, 10, 46), 'available'),
]

def solution_1(snapshots):
    ret = []
    for snapshot_id, created_date, status in snapshots:
        if status == 'available' and snapshot_id.startswith(('butt', 'test')):
            ret.append(snapshot_id)
    return ret

print(solution_1(example_input))


def solution_2(snapshots):
    ret = solution_1(snapshots)

    # NOTE(mcsalgado): I'm normalizing 'months' as date objects with day 1

    current_month = datetime.utcnow().replace(day=1).date()
    current_month = current_month.replace(month=1).replace(year=2017) # assumption of the task!
    previous_month = (current_month - timedelta(days=1)).replace(day=1)
    the_month_before = (previous_month - timedelta(days=1)).replace(day=1)

    months_to_filter_out = (current_month, previous_month, the_month_before)

    for snapshot_id, created_date, status in snapshots:
        created_date_month = created_date.replace(day=1).date()
        if (snapshot_id.startswith('lol') and snapshot_id.endswith('feet')) and (created_date_month not in months_to_filter_out):
            ret.append(snapshot_id)
    return ret

print(solution_2(example_input))


def solution_3(snapshots):
    ret = solution_2(snapshots)

    # NOTE(mcsalgado): I'm normalizing 'months' as date objects with day 1

    current_month = datetime.utcnow().replace(day=1).date()
    current_month = current_month.replace(month=1).replace(year=2017) # assumption of the task!
    previous_month = (current_month - timedelta(days=1)).replace(day=1)
    the_month_before = (previous_month - timedelta(days=1)).replace(day=1)

    months_to_filter_out = (current_month, previous_month, the_month_before)

    # NOTE(mcsalgado): this defaultdict keeps track of possible snapshot candidates segregated by month
    snapshots_by_month = defaultdict(list)

    for snapshot_id, created_date, status in snapshots:
        created_date_month = created_date.replace(day=1).date()
        if snapshot_id.startswith('lol-scene') and (created_date_month not in months_to_filter_out):
            created_date_month = created_date.replace(day=1).date()
            snapshots_by_month[created_date_month].append((created_date, snapshot_id))

    for key, values in snapshots_by_month.items():
        # NOTE(mcsalgado): skip the first snapshot of the month
        for _, snapshot_id in sorted(values)[1:]:
            ret.append(snapshot_id)

    return ret

print(solution_3(example_input))
