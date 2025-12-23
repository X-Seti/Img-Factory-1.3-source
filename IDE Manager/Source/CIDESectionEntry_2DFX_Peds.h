#ifndef CIDESectionEntry_2DFX_Peds_H
#define CIDESectionEntry_2DFX_Peds_H

#include "CIDESectionEntry.h"
#include <string>

struct CIDESectionEntry_2DFX_Peds : public CIDESectionEntry
{
	unsigned long				m_uiObjectId;
	float						m_fPosition[3];
	unsigned char				m_ucColour[3];
	unsigned long				m_uiUnknown1;
	unsigned long				m_ui2dfxType;
	unsigned long				m_uiBehaviour;
	float						m_fUnknown2[3];
	float						m_fPedRotation[3];
};

#endif