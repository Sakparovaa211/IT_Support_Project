
import logging

from django.shortcuts import render, redirect, get_object_or_404

from .models import Ticket
from .forms import TicketForm


# Журнал жүргізу
logger = logging.getLogger(__name__)


# Өтінімдер тізімі
def ticket_list(request):
    tickets = Ticket.objects.all().order_by('-created_at')

    return render(request, 'tickets/ticket_list.html', {
        'tickets': tickets
    })


# Жаңа өтінім қосу
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save()

            # INFO журналы
            logger.info(
                "Өтінім сақталды. ID: %s",
                ticket.id
            )

            return redirect('ticket_list')

        else:
            # WARNING журналы
            logger.warning(
                "Өтінім формасы тексеруден өтпеді"
            )

    else:
        form = TicketForm()

    return render(request, 'tickets/ticket_form.html', {
        'form': form
    })


# Өтінімді жою
def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket_list')

    return render(request, 'tickets/ticket_confirm_delete.html', {
        'ticket': ticket
    })
