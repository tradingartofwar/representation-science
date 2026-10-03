"""One query per process. Reads only JSON stdin; emits no checker feedback."""
import json
import sys
from core import answer, Meter, BudgetExceeded, serialize, F


def main():
    request=json.load(sys.stdin)
    meter=Meter()
    try:
        result=answer(request['payload'],request['question'],request['mode'],
                      request['added_speed'],F(request['threshold']),meter)
    except BudgetExceeded as e:
        result=dict(supported=False,resource_limit=str(e),reason='frozen budget reached')
    result['operations']=dict(sorted(meter.counts.items()))
    result['peak_profile_pieces']=meter.peak_pieces
    print(json.dumps(serialize(result),sort_keys=True,separators=(',',':')))


if __name__=='__main__':
    main()
