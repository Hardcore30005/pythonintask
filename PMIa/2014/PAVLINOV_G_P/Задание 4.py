# ������ 4. ������� 14.
# �������� ���������, ������� ������� ���, ��� ������� ���������� ������ �������� �������. ������������� ���������� ������� ������� ��������� ��������� ��������, ����� ��������, 
# ���� �������� � ������ (���� ������� ����), ��������� ������� �� ������ ������ (��� ������ ������). 
# ��� �������� ���� ����������� ������ ��������� ������������ ����������. ����� ������ ���������� ��������� ������ ���������� ���� ������������ ������ Enter ��� ������.

# ������
# 4.06.2016

name = "������ ��������"
alias = "������ �������� ��������"
dateBirth = 1898
dateDeath = 1940
placeBirth = "����"
hobbies = "���������, ��������, ������������ �������"
ageDeath = dateDeath - dateBirth

print(name+"("+alias+")")
print("����������� ������������: " + hobbies)
print("������� � " + str(dateBirth) + " ����")
print("��������� � " + str(dateDeath) + " ���� "+ "� �������� " +str(ageDeath)+" ���")
input("������� Enter")