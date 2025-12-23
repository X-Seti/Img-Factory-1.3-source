#ifndef CIMGFile_H
#define CIMGFile_H

#include <string>
#include <vector>

struct CIMGEntry;

enum eIMGVersion
{
	IMG_1				= 0,
	IMG_2				= 1,
	IMG_3_ENCRYPTED		= 2,
	IMG_3_UNENCRYPTED	= 3,
	IMG_UNKNOWN			= 4
};

struct CIMGFile
{
	CIMGFile(void) :
		m_bFileFound(false)
	{};

	void							unload(void);

	CIMGEntry*						getEntryByHighestOffset(void);
	unsigned long					getVersion3NamesLength(void);
	CIMGEntry*						getEntryByName(std::string strEntryName);
	CIMGEntry*						getEntryByNameWithoutExtension(std::string strEntryNameWithoutExtension);
	unsigned long					getEntryIndex(CIMGEntry *pIMGEntry);

	bool							m_bFileFound;
	std::string						m_strPath;

	eIMGVersion						m_eVersion;
	unsigned long					m_uiEntryCount;
	std::vector<CIMGEntry*>			m_vecEntries;

	//std::string						m_strIMGContent;
	//std::string*					m_pIMGContent;
};

#endif