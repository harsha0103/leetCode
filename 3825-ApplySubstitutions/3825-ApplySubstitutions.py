# Last updated: 6/25/2026, 9:09:49 AM
class Solution(object):
    def applySubstitutions(self, replacements, text):
        """
        :type replacements: List[List[str]]
        :type text: str
        :rtype: str
        """
        split_text=text.split('_')
        result=''
        d={'%'+i[0]+'%':i[1] for i in replacements}
       

        for i in split_text:
            result=result+'_'+d[i]
        while '%' in result:
            for i in split_text:
                result=result.replace(i,d[i],1)


        return(result.replace('_','',1))