from django.db import models

class MonthlyReport(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()
    total_donations = models.DecimalField(max_digits=10, decimal_places=2)

from django.db.models import Sum
from datetime import datetime
from django.utils import timezone
from collectApp.models import DonationTicket


def calculate_monthly_donations(month, year):
    start_date = datetime(year, month, 1)
    end_date = start_date.replace(month=start_date.month % 12 + 1, day=1) if month != 12 else start_date.replace(year=start_date.year + 1, month=1, day=1)
    total_donations = DonationTicket.objects.filter(createdAt__gte=start_date, createdAt__lt=end_date).aggregate(Sum('available_food_count'))['available_food_count__sum'] or 0
    return total_donations



def generate_monthly_reports():
    current_month = timezone.now().month
    current_year = timezone.now().year
    total_donations = calculate_monthly_donations(current_month, current_year)
    report = MonthlyReport.objects.create(month=current_month, year=current_year, total_donations=total_donations)
    report.save()
