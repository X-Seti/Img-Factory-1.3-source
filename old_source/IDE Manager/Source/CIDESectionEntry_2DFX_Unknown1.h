#ifndef CIDESectionEntry_2DFX_Unknown1_H
#define CIDESectionEntry_2DFX_Unknown1_H

#include "CIDESectionEntry.h"
#include <string>

struct CIDESectionEntry_2DFX_Unknown1 : public CIDESectionEntry
{
	unsigned long				m_uiObjectId;
	float						m_fPosition[3];
	unsigned char				m_ucColour[3];
	unsigned long				m_uiUnknown1;
	unsigned long				m_ui2dfxType;
	unsigned long				m_uiUnknown2;
	float						m_fUnknown3[3];
	unsigned long				m_uiUnknown4;
};

#endif