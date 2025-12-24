#ifndef CFileUtility_H
#define CFileUtility_H

#include <string>

class CFileUtility
{
public:
	static std::string			getFileContent(std::string strPath, bool bBinaryMode = true);
	static std::string*			getFileContentPointer(std::string strPath, bool bBinaryMode = true);
	static std::string			getFileSubContent(std::string strPath, unsigned long uiSeek, unsigned long uiByteCount, bool bBinaryMode = true);
	static unsigned long		getFileSize(std::string& strPath);
	static void					storeFile(std::string strPath, std::string strData, bool bAppend = true, bool bBinaryMode = true);
	static void					storeFileByStringPointer(std::string strPath, std::string* pData, bool bAppend = true, bool bBinaryMode = true);
	static void					renameFile(std::string strPath, std::string strNewPath);
	static void					removeFile(std::string strPath);
	static std::string			getFileNameFromNameWithoutExtension(std::string strFolderPath, std::string strFileNameWithoutExtension);
};

#endif