#include "CRegistryUtility.h"
#include "CStringUtility.h"
#include <Windows.h>

using namespace std;

void			CRegistryUtility::setRegistryValueString(string strKey1, string strKey2, string strValue)
{
	HKEY hKey;
	if (RegOpenKeyEx(HKEY_CURRENT_USER, CStringUtility::convertStdStringToStdWString(strKey1).c_str(), NULL, KEY_ALL_ACCESS, &hKey) == ERROR_FILE_NOT_FOUND)
	{
		RegCreateKeyEx(HKEY_CURRENT_USER, CStringUtility::convertStdStringToStdWString(strKey1).c_str(), NULL, NULL, REG_OPTION_NON_VOLATILE, KEY_ALL_ACCESS, NULL, &hKey, NULL);
	}
	RegSetValueEx(hKey, CStringUtility::convertStdStringToStdWString(strKey2).c_str(), 0, REG_SZ, (BYTE*)CStringUtility::convertStdStringToStdWString(strValue).c_str(), strValue.length()*sizeof(wchar_t));
	RegCloseKey(hKey);
}

string			CRegistryUtility::getRegistryValueString(string strKey1, string strKey2)
{
	wchar_t szBuffer[MAX_PATH];
	DWORD uiBufferSize = MAX_PATH;

	HKEY hKey;
	if (RegOpenKey(HKEY_CURRENT_USER, CStringUtility::convertStdStringToStdWString(strKey1).c_str(), &hKey) != ERROR_SUCCESS)
	{
		return "";
	}
	if (RegQueryValueEx(hKey, CStringUtility::convertStdStringToStdWString(strKey2).c_str(), NULL, NULL, (LPBYTE)szBuffer, &uiBufferSize) != ERROR_SUCCESS)
	{
		return "";
	}
	RegCloseKey(hKey);

	szBuffer[uiBufferSize] = '\0';

	string strData = CStringUtility::convertStdWStringToStdString(szBuffer);
	return strData;
}

void			CRegistryUtility::setRegistryValueInt(string strKey1, string strKey2, int iValue)
{
	HKEY hKey;
	if (RegOpenKeyEx(HKEY_CURRENT_USER, CStringUtility::convertStdStringToStdWString(strKey1).c_str(), NULL, KEY_ALL_ACCESS, &hKey) == ERROR_FILE_NOT_FOUND)
	{
		RegCreateKeyEx(HKEY_CURRENT_USER, CStringUtility::convertStdStringToStdWString(strKey1).c_str(), NULL, NULL, REG_OPTION_NON_VOLATILE, KEY_ALL_ACCESS, NULL, &hKey, NULL);
	}
	RegSetValueEx(hKey, CStringUtility::convertStdStringToStdWString(strKey2).c_str(), 0, REG_DWORD, (BYTE*)&iValue, 4);
	RegCloseKey(hKey);
}

int				CRegistryUtility::getRegistryValueInt(string strKey1, string strKey2)
{
	DWORD uiValue = 0;
	DWORD uiBufferSize = 4;

	HKEY hKey;
	if (RegOpenKeyEx(HKEY_CURRENT_USER, CStringUtility::convertStdStringToStdWString(strKey1).c_str(), 0, KEY_READ, &hKey) != ERROR_SUCCESS)
	{
		return 0;
	}
	if (RegQueryValueEx(hKey, CStringUtility::convertStdStringToStdWString(strKey2).c_str(), NULL, NULL, (LPBYTE)&uiValue, &uiBufferSize) != ERROR_SUCCESS)
	{
		return 0;
	}
	RegCloseKey(hKey);

	return uiValue;
}