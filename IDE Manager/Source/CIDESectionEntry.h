#ifndef CIDESectionEntry_H
#define CIDESectionEntry_H

#include "eIDEFileSection.h"
#include <string>
#include <vector>

class CIDESectionEntry
{
public:
	std::string					m_strComment;				// the comment at the end of the line.
	std::string*				m_pPreviousComment;			// the latest comment found on a previous line.
	std::vector<std::string>	m_vecPreviousCommentLines;	// the comments on the line(s) directly before this section entry.
	unsigned long				m_uiOldObjectId;
	eIDEFileSection				m_eSectionType;
};

#endif