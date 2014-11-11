# coding=utf-8

from datetime import *
import copy

def submissionData(course, start=datetime.min, end=datetime.max):
  buckets = {}
  for d in range(7):
    for h in range(24):
      buckets[(d,h)] = 0
  for a in course.assignments:
    for p in a.problems:
      for sl in p.studentSubmissions.values():
        for s in sl.submissions:
          if s.submissionTime > start and s.submissionTime < end:
            key = (s.submissionTime.weekday(), s.submissionTime.hour)
            buckets[key] += 1

  outList = []
  for k, v in buckets.iteritems():
    outList.append([k[0], k[1], v])
  return outList


def attendanceBuckets(course, start=datetime.min, end=datetime.max):
  pass