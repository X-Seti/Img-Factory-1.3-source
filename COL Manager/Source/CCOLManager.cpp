#include "CCOLManager.h"
#include "CCOLFile.h"
#include "CCOLEntry.h"
#include "CFileParser.h"
#include "CFileWriter.h"
#include "CStringUtility.h"

using namespace std;

CCOLManager*	CCOLManager::m_pInstance = nullptr;

CCOLManager*	CCOLManager::getInstance(void)
{
	if (CCOLManager::m_pInstance == nullptr)
	{
		CCOLManager::m_pInstance = new CCOLManager;
	}
	return CCOLManager::m_pInstance;
}


CCOLFile*		CCOLManager::parseFile(string strPath)
{
	CFileParser::getInstance()->setReadAllAtOnce(true);
	bool bFileFound = CFileParser::getInstance()->open(strPath, true);
	unsigned long uiSeek = 0;

	CCOLFile *pCOLFile = new CCOLFile;
	pCOLFile->m_strFilePath = strPath;
	if (!bFileFound)
	{
		return pCOLFile;
	}

	do
	{
		string strBytes = CFileParser::getInstance()->readString(72);

		CCOLEntry *pEntry = new CCOLEntry;
		pCOLFile->m_vecEntries.push_back(pEntry);

		pEntry->m_strVersion					= strBytes.substr(0, 4);
		pEntry->m_uiFileSize					= CStringUtility::unpackULong(strBytes.substr(4, 4), false);
		pEntry->m_strModelName					= CStringUtility::rtrim(strBytes.substr(8, 22));
		pEntry->m_usModelId						= CStringUtility::unpackUShort(strBytes.substr(30, 2), false);
		pEntry->m_strTBounds					= strBytes.substr(32, 40);

		if (pEntry->m_strVersion == "COL2" || pEntry->m_strVersion == "COL3")
		{
			pEntry->m_strHeaderVersion2 = CFileParser::getInstance()->readString(36);

			if(pEntry->m_strVersion == "COL3")
			{
				pEntry->m_strHeaderVersion3 = CFileParser::getInstance()->readString(16);
				pEntry->m_uiBodyStart = uiSeek + 124;
				pEntry->m_uiBodyLength = (pEntry->m_uiFileSize + 8) - 124;
			}
			else
			{
				pEntry->m_uiBodyStart = uiSeek + 108;
				pEntry->m_uiBodyLength = (pEntry->m_uiFileSize + 8) - 108;
			}
		}
		else
		{
			pEntry->m_uiBodyStart = uiSeek + 72;
			pEntry->m_uiBodyLength = (pEntry->m_uiFileSize + 8) - 72;
		}

		uiSeek += pEntry->m_uiFileSize + 8;
	}
	while (!CFileParser::getInstance()->isEOF());

	CFileParser::getInstance()->close();

	return pCOLFile;
}

/*
void		CCOLManager::storeFile(CCOLFile *pCOLFile)
{
	string strCOLContents = getGTATools()->getFileParser()->readContents("../" + pCOLFile->m_strFilePath);
	getGTATools()->getFileWriter()->openBinaryFile(pCOLFile->m_strFilePath);
	for (auto pEntry : pCOLFile->m_vecEntries)
	{
		getGTATools()->getFileWriter()->writeString(pEntry->m_strVersion, 4);
		getGTATools()->getFileWriter()->writeULong(pEntry->m_uiFileSize);
		getGTATools()->getFileWriter()->writeString(CStringUtility::zeroPad(pEntry->m_strModelName, 22), 22);
		getGTATools()->getFileWriter()->writeUShort(pEntry->m_usModelId);
		getGTATools()->getFileWriter()->writeString(CStringUtility::zeroPad(pEntry->m_strTBounds, 40), 40);

		if (pEntry->m_strVersion == "COL2" || pEntry->m_strVersion == "COL3")
		{
			getGTATools()->getFileWriter()->writeString(pEntry->m_strHeaderVersion2, 36);

			if (pEntry->m_strVersion == "COL3")
			{
				getGTATools()->getFileWriter()->writeString(pEntry->m_strHeaderVersion3, 16);
			}
		}

		getGTATools()->getFileWriter()->writeString(strCOLContents.substr(pEntry->m_uiBodyStart, pEntry->m_uiBodyLength), pEntry->m_uiBodyLength);
	}
	getGTATools()->getFileWriter()->closeBinaryFile();
}
*/