%if results:
<table border="1" cellpadding="1" cellspacing="0">
<thead>
<tr>
    <th>Time First</th>
    <th>Time Last</th>
    <th>Address</th>
    <th>Confidence</th>
    <th>Description</th>
    <th>Tags</th>
    <th>Alternative ID</th> 
</tr>
</thead>
<tbody>
%for r in results:
<tr>
    <td> ${r['reporttime']}     </td>
    <td> ${r['lasttime']}      </td>
    <td class="arg"> ${r['observable']}        </td>
    <td> ${r['confidence']}        </td>
    <td> ${r.get('description','')}    </td>
    <td> ${','.join(r.get('tags',[]))}    </td>
    <td> ${r.get('altid','')}  </td>
</tr>
%endfor
</tbody>
</table>
%endif
