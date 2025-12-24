#ifndef CIMGEntry_H
#define CIMGEntry_H

#include <string>

struct CIMGEntry
{
	CIMGEntry(void) :
		m_uiResourceType(0),
		m_uiVersion(0),
		m_usFlags(0)
	{};

	unsigned long		m_uiFileOffset; // in blocks (2048 bytes)
	unsigned long		m_uiFileSize; // in bytes
	std::string			m_strFileName;
	unsigned long		m_uiVersion;
	unsigned long		m_uiResourceType;
	unsigned short		m_usFlags;

	unsigned long		m_uiNewFileOffset;
};

#endif