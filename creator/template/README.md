# {{ question.title }}

*[Data Stewardship Wizard] Question - additional resources*

Short UID: {{ question.shortuid }}

## The Question

{% if question.text is not none %}{{ question.text }}{% else %}{{ question.title }}{% endif %}
{% if question.type == 'option' %}
### Possible answers:
{% for answer in question.answers %}
  * {{ answer.label }} {% if answer.advice is not none %}(*Advice*: {{ answer.advice }}){% endif %}{% endfor %}
{% endif %}
## Links

  * [Resources page in DSW]
  * [Data Stewardship Wizard]
  * [DSW @ GitHub]
{% for ref in question.references %}  * [{{ ref.anchor }}]({{ ref.url }}){% endfor %}

## Resources tips

  * If you have any ideas, please go to [issues].
  * You can provide any extra resources in the `/resources` directory via [pull request].

----

*Do not edit this README file by hand, it is automatically generated*

[Data Stewardship Wizard]: https://dmp.fairdata.solutions
[Resources page in DSW]: https://dmp.fairdata.solutions/resources/{{ question.shortuid }}
[DSW @ GitHub]: https://github.com/DataStewardshipWizard
[issues]: https://help.github.com/articles/about-issues/
[pull request]: https://help.github.com/articles/about-pull-requests/
