from django.views.generic import TemplateView
from django.views.generic import FormView

from .forms import ChatBotForm
from .kenji_bot import respond

qa = {
    "question": "",
    "answer": "",
}

class IndexView(FormView):
    template_name = "index.html"
    form_class = ChatBotForm
    success_url = 'index'

    def form_valid(self, form):
        qa["question"] = form.data.get("question")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        if len(qa["question"]) > 0:
            qa["answer"] = respond(qa["question"])

        context = super().get_context_data(**kwargs)
        context['question'] = qa["question"]
        context['answer'] = qa["answer"]
        return context

class AboutView(TemplateView):
    template_name = "about.html"