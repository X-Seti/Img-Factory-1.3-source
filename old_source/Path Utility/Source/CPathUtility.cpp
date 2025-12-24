#include "CPathUtility.h"
#include "CStringUtility.h"

using namespace std;

string			CPathUtility::getFileName(string strPath)
{
	strPath = CStringUtility::replace(strPath, "\\", "/");
	size_t uiPosition = strPath.find_last_of("/");
	if (uiPosition == string::npos)
	{
		return strPath;
	}
	return strPath.substr(uiPosition + 1);
}

string			CPathUtility::getFileExtension(string strPath)
{
	size_t uiPosition = strPath.find_last_of(".");
	if (uiPosition == string::npos)
	{
		return "";
	}
	return strPath.substr(uiPosition + 1);
}

string			CPathUtility::replaceExtension(string strPath, string strExtension)
{
	size_t uiPosition = strPath.find_last_of(".");
	if (uiPosition == string::npos)
	{
		return strPath + "." + strExtension;
	}
	return strPath.substr(0, uiPosition + 1) + strExtension;
}

string			CPathUtility::removeExtension(string strPath)
{
	size_t uiPosition = strPath.find_last_of(".");
	if (uiPosition == string::npos)
	{
		return strPath;
	}
	return strPath.substr(0, uiPosition);
}

string			CPathUtility::addSlashToEnd(string strPath)
{
	if (strPath.c_str()[strPath.length() - 1] != '\\' && strPath.c_str()[strPath.length() - 1] != '/')
	{
		strPath += "/";
	}
	return strPath;
}