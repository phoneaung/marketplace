from django.shortcuts import render, get_object_or_404

from item.models import Item

from .forms import ConversationMessageForm 
from .models import Conversation, ConversationMessage

def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    # check  if you are the owner of the item, you should not be able to visit this page
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    # if the id is one of the members, then proceed  
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id]) 

    # if there is a conversation with the owner/user already, then redirect to that conversation page
    if conversations:
        pass

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user

            return redirect('item:detail', pk=item_pk)
        
        else:
            form = ConversationMessageForm()

        return render(request, 'conversation/new.html', {
            'form': form
        })