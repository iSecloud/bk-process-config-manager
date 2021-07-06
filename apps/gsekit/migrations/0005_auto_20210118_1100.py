# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸 (Blueking) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""
# Generated by Django 2.2.6 on 2021-01-18 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gsekit", "0004_auto_20210115_2002"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job", name="expression", field=models.TextField(null=True, verbose_name="实例表达式"),
        ),
    ]
