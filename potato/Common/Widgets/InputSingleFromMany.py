from django.forms.widgets import Input
from django.utils.html import mark_safe

class InputSingleFromMany(Input):
    """
    Fields like MedicationRequest.medication_cc expect multiple
    because CodeableConcepts are ManyToMany fields
    but we just want to choose one (like a basic input with datalist)
    so this returns a list with only one single item [value]
    """
    input_type = 'hidden'

    def render(self, name, value, attrs=None, renderer=None):
        if value is not None and isinstance(value, (list, tuple)) and len(value) == 1:
            value = value[0]
            
        final_attrs = self.build_attrs(self.attrs, attrs)
        hidden_input = super().render(name, value, final_attrs, renderer)
        
        current_label = next((label for val, label in self.choices if str(val) == str(value)), '')
        widget_id = final_attrs.get('id', name)
        
        options_html = '\n'.join(f'<option value="{label}" data-id="{val}">' for val, label in self.choices)
        
        html = f"""
            {hidden_input}
            <input type="text" 
                   value="{current_label}"
                   list="{name}-list"
                   autocomplete="off"
                   placeholder="🔍"
                   id="{name}-display">
            <datalist id="{name}-list">
                {options_html}
            </datalist>
            <script>
            document.getElementById('{name}-display').addEventListener('blur', function() {{
                const val = this.value.trim().toLowerCase();
                if (!val) {{
                    this.value = '';
                    document.getElementById('{widget_id}').value = '';
                    return;
                }}
                const opts = document.querySelectorAll('#{name}-list option');
                for (let opt of opts) {{
                    if (opt.value.toLowerCase().includes(val)) {{
                        this.value = opt.value;
                        document.getElementById('{widget_id}').value = opt.dataset.id;
                        return;
                    }}
                }}
                this.value = '';
                document.getElementById('{widget_id}').value = '';
            }});
            </script>
            <style>
            input::placeholder {{
                text-align: right;
            }}
            </style>
        """
        return mark_safe(html)

    def value_from_datadict(self, data, files, name):
        value = super().value_from_datadict(data, files, name)
        if value:
            return [value]
        return [] 