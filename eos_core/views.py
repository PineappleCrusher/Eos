#    Copyright © 2017  RunasSudo (Yingtong Li)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import eos_core.models
import eos_core.objects
import eos_core.workflow

import django.http
import django.shortcuts

def index(request):
	return django.shortcuts.render(request, 'eos_core/index.html', {'workflow_tasks': eos_core.workflow.WorkflowTask.get_all() })

def election_json(request, election_id):
	election = django.shortcuts.get_object_or_404(eos_core.models.Election, id=election_id)
	return django.http.HttpResponse(eos_core.objects.to_json(eos_core.objects.EosObject.serialise_and_wrap(election, None, request.GET.get('hashed', 'false') == 'true')), content_type='application/json')
