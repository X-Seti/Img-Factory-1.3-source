#include "CIMGFile.h"
#include "CIMGEntry.h"
#include "CStringUtility.h"
#include "CPathUtility.h"

using namespace std;

void					CIMGFile::unload(void)
{
	for (auto pEntry : m_vecEntries)
	{
		delete pEntry;
	}
}

CIMGEntry*				CIMGFile::getEntryByHighestOffset(void)
{
	unsigned long uiHighestOffset = 0;
	CIMGEntry *pHighestOffsetIMGEntry = nullptr;
	for(auto pIMGEntry : m_vecEntries)
	{
		if(pIMGEntry->m_uiFileOffset > uiHighestOffset)
		{
			uiHighestOffset = pIMGEntry->m_uiFileOffset;
			pHighestOffsetIMGEntry = pIMGEntry;
		}
	}
	return pHighestOffsetIMGEntry;
}

unsigned long			CIMGFile::getVersion3NamesLength(void)
{
	unsigned long uiLength = 0;
	for (auto pEntry : m_vecEntries)
	{
		uiLength += pEntry->m_strFileName.length();
	}
	uiLength += m_vecEntries.size();
	return uiLength;
}

CIMGEntry*				CIMGFile::getEntryByName(string strEntryName)
{
	for (auto pEntry : m_vecEntries)
	{
		if (CStringUtility::toUpperCase(strEntryName) == CStringUtility::toUpperCase(pEntry->m_strFileName))
		{
			return pEntry;
		}
	}
	return nullptr;
}

CIMGEntry*				CIMGFile::getEntryByNameWithoutExtension(string strEntryNameWithoutExtension)
{
	for (auto pEntry : m_vecEntries)
	{
		if (CStringUtility::toUpperCase(strEntryNameWithoutExtension) == CStringUtility::toUpperCase(CPathUtility::removeExtension(pEntry->m_strFileName)))
		{
			return pEntry;
		}
	}
	return nullptr;
}

unsigned long			CIMGFile::getEntryIndex(CIMGEntry *pIMGEntry)
{
	for (unsigned long i = 0; i < m_vecEntries.size(); i++)
	{
		if (m_vecEntries[i] == pIMGEntry)
		{
			return i;
		}
	}
	return -1;
}