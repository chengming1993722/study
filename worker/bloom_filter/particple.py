def major_segments(s):
    major_breaks = ' '
    last = -1
    results = set()
    for idx,ch in enumerate(s):
        if ch in major_breaks:
            segment = s[last+1:idx]
            results.add(segment)
            last = idx
    segment = s[last+1:]
    results.add(segment)
    return results


def minor_segments(s):
    minor_breaks = '_.'
    last = -1
    results = set()
    count = 0
    for idx,ch in enumerate(s):
        if ch in minor_breaks:
            segment = s[last+1:idx]
            results.add(segment)
            segment = s[:idx]
            results.add(segment)
            last = idx
            count+=1
    segment = s[last+1:]
    results.add(segment)
    results.add(s)
    return results

def segments(event):
    results = set()
    for majior in minor_segments(event):
        for minor in major_segments(majior):
            results.add(minor)
    return results

