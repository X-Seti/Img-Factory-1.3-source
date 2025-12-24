#ifndef CIMGManager_H
#define CIMGManager_H

#include "CIMGFile.h"
#include <string>
#include <vector>

class CIMGManager
{
public:
	static CIMGManager*	getInstance(void);

	CIMGFile*			parseFile(std::string strIMGPath, eIMGVersion eIMGVersion);
	void				storeFile(CIMGFile *pIMGFile, std::string strIMGPath);

	CIMGFile*			parseIMG_Version1(std::string strIMGPath);
	CIMGFile*			parseIMG_Version2(std::string strIMGPath);
	CIMGFile*			parseIMG_Version3Encrypted(std::string strIMGPath);
	CIMGFile*			parseIMG_Version3Unencrypted(std::string strIMGPath);

	void				storeIMG_Version1(CIMGFile *pIMGFile, std::string strIMGPath);
	void				storeIMG_Version2(CIMGFile *pIMGFile, std::string strIMGPath);
	void				storeIMG_Version3Encrypted(CIMGFile *pIMGFile, std::string strIMGPath);
	void				storeIMG_Version3Unencrypted(CIMGFile *pIMGFile, std::string strIMGPath);

	void				mergeIMG(CIMGFile *pIMGFile, std::string strPath);
	void				splitIMG(std::vector<CIMGEntry*>& vecIMGEntries, std::string strPath, eIMGVersion eIMGVersion);
	unsigned long		replaceEntries(CIMGFile *pIMGFile, std::vector<std::string>& vecPaths);
	void				loadRWVersionsFromFile(CIMGFile *pIMGFile);
	void				exportEntries(CIMGFile *pIMGFile, std::vector<CIMGEntry*>& vecIMGEntries, std::string strFolderPath);

	static std::string	getRWVersionName(unsigned long uiVersion);
	static std::string	getIMGVersionName(eIMGVersion eVersion);
	static std::string	getResouceTypeName(unsigned long uiResourceType);
	static eIMGVersion	getIMGVersion(std::string& strPath);
	static std::string	encryptString(std::string strData);
	static std::string	decryptString(std::string strData);

private:
	static CIMGManager*	m_pInstance;
};

#endif