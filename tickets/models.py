from django.db import models


class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ("Төмен", "Төмен"),
        ("Орташа", "Орташа"),
        ("Жоғары", "Жоғары"),
    ]
    STATUS_CHOICES = [
        ("Жаңа", "Жаңа"),
        ("Орындалуда", "Орындалуда"),
        ("Аяқталды", "Аяқталды"),
    ]

    title = models.CharField("Тақырып", max_length=150)
    description = models.TextField("Сипаттама")
    priority = models.CharField("Басымдық", max_length=20, choices=PRIORITY_CHOICES, default="Орташа")
    status = models.CharField("Мәртебе", max_length=20, choices=STATUS_CHOICES, default="Жаңа")
    created_at = models.DateTimeField("Құрылған уақыты", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Өтінім"
        verbose_name_plural = "Өтінімдер"

    def __str__(self):
        return self.title
