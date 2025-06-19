from django.contrib import admin
from django.utils.html import format_html
from .models import QuestionPaper

@admin.action(description="Approve selected papers")
def approve_papers(modeladmin, request, queryset):
    queryset.update(is_approved=True)

@admin.action(description="Reject selected papers")
def reject_papers(modeladmin, request, queryset):
    queryset.update(is_approved=False)

@admin.register(QuestionPaper)
class QuestionPaperAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'year', 'faculty', 'approval_status', 'uploaded_at')
    list_filter = ('year', 'is_approved', 'faculty', 'slot')
    search_fields = ('course_name', 'course_code', 'faculty')
    actions = [approve_papers, reject_papers]

    def approval_status(self, obj):
        if obj.is_approved:
            return format_html('<span style="color:green;">✅ Approved</span>')
        else:
            return format_html('<span style="color:red;">❌ Not Approved</span>')

    approval_status.short_description = "Approval Status"
