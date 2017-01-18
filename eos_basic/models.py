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

# A type of question which permits voters to place check marks against the names of a specified number of candidates
class ApprovalQuestion(eos_core.objects.EosDictObject, eos_core.models.Question):
	class EosMeta:
		eos_name = 'eos_basic.models.ApprovalQuestion'
		eos_fields = [
			eos_core.objects.EosField(str, 'title'),
			eos_core.objects.EosField(str, 'description'),
			eos_core.objects.EosField(list, 'choices', element_type=eos_core.objects.EosField(str)),
			eos_core.objects.EosField(int, 'max_choices'),
			eos_core.objects.EosField(int, 'min_choices')
		]

# All registered users are eligible to vote in this election
class UnconditionalVoterEligibility(eos_core.models.VoterEligibility, eos_core.objects.EosObject):
	class EosMeta:
		eos_name = 'eos_basic.models.UnconditionalVoterEligibility'
	
	def serialise(self, hashed=False):
		return None
	
	@staticmethod
	def _deserialise(cls, value):
		return cls()