from bs4 import BeautifulSoup

html_content = '''
<tr>
    <td style="word-break:break-all; padding:3px;" bgcolor="#ffffff" class="listData" align="right">281</td>
    <td style="word-break:break-all; padding:3px;" bgcolor="#ffffff" class="listData">tech3rd</td>
    <td style="word-break:break-all; padding:3px;" bgcolor="#ffffff" class="listData">
        <div align="center">---</div>
    </td>
    <td style="word-break:break-all; padding:3px;" bgcolor="#ffffff" class="listData">C:\Aplsys\auto_print_wms3\temp\G0211154101.pdf</td>
    <td style="word-break:break-all; padding:3px;" bgcolor="#ffffff" class="listData">
        <div nowrap>Print Complete</div>
    </td>
    <td style="word-break:break-all; padding:3px;" bgcolor="#ffffff" class="listData">
        <nobr>19/1/2024</nobr>
        <nobr> 12:48:17</nobr>
    </td>
    <td style="word-break:break-all; padding:3px;" bgcolor="#ffffff" class="listData" align="right">2</td>
</tr>
'''

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the specific cell containing the file path
file_path_cell = soup.find('td', {'class': 'listData', 'style': 'word-break:break-all; padding:3px;'})

# Extract the text from the file path cell
file_path_text = file_path_cell.get_text(strip=True)

# Extract the text index
text_index = file_path_text.split('\\')[-1].split('.')[0]

print(text_index)
