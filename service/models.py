from django.db import models

TASK_STATUSES = [('created', 'created'), ('working', 'working'), ('finished', 'finished')]

TASK_TYPES = [('metrica', 'metrica'), ('direct', 'direct')]


class Site(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'


class Task(models.Model):
    workingIntervalStart = models.DateTimeField()
    workingIntervalEnd = models.DateTimeField()
    dateOfCreation = models.DateTimeField(auto_now_add=True)
    dateOfEnd = models.DateTimeField()
    status = models.CharField(max_length=60, choices=TASK_STATUSES)
    type = models.CharField(max_length=60, choices=TASK_TYPES)
    sites = models.ManyToManyField(Site)

    def get_sites(self):
        return "\n".join([s.name for s in self.sites.all()])

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class File(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
