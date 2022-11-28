# Generated by Django 4.1.3 on 2022-11-28 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("surveys", "0002_answer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="answer",
            name="question_item",
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="surveys.question",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="question",
            name="checkbox_content",
            field=models.JSONField(default=dict, verbose_name="CheckboxData"),
        ),
        migrations.AddField(
            model_name="question",
            name="dropdown_content",
            field=models.JSONField(default=dict, verbose_name="DropdownData"),
        ),
        migrations.AddField(
            model_name="question",
            name="paragraph_content",
            field=models.CharField(default=None, max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="question",
            name="radio_content",
            field=models.JSONField(default=dict, verbose_name="RadioData"),
        ),
        migrations.AddField(
            model_name="question",
            name="short_answer_content",
            field=models.CharField(default=None, max_length=400),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="QuestionItem",
        ),
    ]
