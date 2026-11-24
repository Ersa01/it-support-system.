import logging

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TicketForm
from .models import Ticket

logger = logging.getLogger(__name__)


def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets/ticket_list.html", {"tickets": tickets})


def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            logger.info("Өтінім сақталды: ID=%s", ticket.id)
            messages.success(request, "Өтінім сәтті тіркелді.")
            return redirect("ticket_list")
        logger.warning("Өтінім формасы тексеруден өтпеді")
    else:
        form = TicketForm()
    return render(request, "tickets/ticket_form.html", {"form": form, "page_title": "Жаңа өтінім"})


def ticket_update(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, "Өтінім жаңартылды.")
            return redirect("ticket_list")
        logger.warning("Өтінім формасы тексеруден өтпеді")
    else:
        form = TicketForm(instance=ticket)
    return render(request, "tickets/ticket_form.html", {"form": form, "page_title": "Өтінімді өзгерту"})


def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        ticket.delete()
        messages.success(request, "Өтінім жойылды.")
        return redirect("ticket_list")
    return render(request, "tickets/ticket_confirm_delete.html", {"ticket": ticket})
