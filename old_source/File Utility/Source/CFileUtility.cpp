#include "CFileUtility.h"
#include "CPathUtility.h"
#include <fstream>
#include <Windows.h>

using namespace std;

string		CFileUtility::getFileContent(string strPath, bool bBinaryMode)
{
	ifstream t(strPath.c_str(), bBinaryMode ? ios::in | ios::binary : ios::in);
	if (!t.is_open())
	{
		return "";
	}
	t.seekg(0, ios::end);
	size_t size = t.tellg();
	string buffer(size, ' ');
	t.seekg(0);
	t.read(&buffer[0], size);
	t.close();
	return buffer;
}
string*			CFileUtility::getFileContentPointer(string strPath, bool bBinaryMode)
{
	string *pData = new string;

	ifstream t(strPath.c_str(), bBinaryMode ? (ios::in | ios::binary) : ios::in);
	if (!t.is_open())
	{
		*pData = "";
		return pData;
	}
	t.seekg(0, ios::end);
	size_t size = t.tellg();
	pData->resize(size, '\0');
	t.seekg(0, ios::beg);
	t.read(&(*pData)[0], size);
	t.close();
	return pData;
}
string			CFileUtility::getFileSubContent(string strPath, unsigned long uiSeek, unsigned long uiByteCount, bool bBinaryMode)
{
	ifstream t(strPath.c_str(), bBinaryMode ? ios::in | ios::binary : ios::in);
	if (!t.is_open())
	{
		return "";
	}
	t.seekg(uiSeek, ios::beg);
	string buffer(uiByteCount, ' ');
	t.read(&buffer[0], uiByteCount);
	t.close();
	return buffer;
}

unsigned long	CFileUtility::getFileSize(string& strPath)
{
	FILE *pFile;
	fopen_s(&pFile, strPath.c_str(), "rb");
	fseek(pFile, 0, SEEK_END);
	unsigned long iSeek = ftell(pFile);
	fclose(pFile);
	return iSeek;
}

void			CFileUtility::storeFile(string strPath, string strData, bool bAppend, bool bBinaryMode)
{
	//createFoldersForPath(strPath);
	FILE *pFile;
	fopen_s(&pFile, strPath.c_str(), (string((bAppend ? "a" : "w")) + string((bBinaryMode ? "b" : ""))).c_str());
	fwrite(strData.c_str(), 1, strData.length(), pFile);
	fclose(pFile);
}

void			CFileUtility::storeFileByStringPointer(string strPath, string* pData, bool bAppend, bool bBinaryMode)
{
	FILE *pFile;
	fopen_s(&pFile, strPath.c_str(), (string((bAppend ? "a" : "w")) + string((bBinaryMode ? "b" : ""))).c_str());
	fwrite(pData->c_str(), 1, pData->length(), pFile);
	fclose(pFile);
}

void			CFileUtility::renameFile(string strPath, string strNewPath)
{
	rename(strPath.c_str(), strNewPath.c_str());
}

void			CFileUtility::removeFile(string strPath)
{
	//remove(strPath.c_str());
	DeleteFile(strPath.c_str());
}

string			CFileUtility::getFileNameFromNameWithoutExtension(string strFolderPath, string strFileNameWithoutExtension)
{
	CPathUtility::addSlashToEnd(strFolderPath);
	strFolderPath += "*";

	WIN32_FIND_DATAA ffd;
	HANDLE hFind = FindFirstFile(strFolderPath.c_str(), &ffd);
	if (hFind == INVALID_HANDLE_VALUE)
	{
		return "";
	}

	do
	{
		if (CPathUtility::removeExtension(ffd.cFileName) == strFileNameWithoutExtension)
		{
			FindClose(hFind);
			return strFolderPath + ffd.cFileName;
		}
	}
	while (FindNextFile(hFind, &ffd) != 0);

	FindClose(hFind);
	return "";
}