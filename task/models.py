# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    description = models.TextField(verbose_name=u'描述')
    completed = models.BooleanField(verbose_name=u'是否完成', default=False)
    create_date = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.title







