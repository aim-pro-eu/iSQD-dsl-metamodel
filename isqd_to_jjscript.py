import json

json_data = json.load(open('isqd.json', 'r'))

TEMPLATE = """do
create class {synthesis} extends PedagogicalStrategy
create abstract class {synthesis}Activity
create containment activities in {synthesis} type {synthesis}Activity [1..*]
{activities}
end
"""

ACTIVITY_TEMPLATE = """create class {activity}
{activity} extends {synthesis}Activity
{activity} extends PedagogicalActivity"""

for s in json_data:
    synthesis = s['synthesis']
    activities = ""
    for a in s['subcategories']:
        activities += ACTIVITY_TEMPLATE.format(activity=a, synthesis=synthesis) + "\n"
    script = TEMPLATE.format(synthesis=synthesis, activities=activities)
    print(script)
    print("\n\n")