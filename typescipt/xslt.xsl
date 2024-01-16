<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/form">
    <html>
      <head>
        <title><xsl:value-of select="@string"/></title>
      </head>
      <body>
        <form action="/submit" method="post">
          <fieldset>
            <legend><xsl:value-of select="@string"/></legend>
            <xsl:apply-templates select="sheet/group"/>
            <button type="submit">Submit</button>
          </fieldset>
        </form>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="group">
    <div class="group">
      <xsl:apply-templates select="field"/>
    </div>
  </xsl:template>

  <xsl:template match="field">
    <label for="{@name}"><xsl:value-of select="@name"/></label>
    <input type="text" id="{@name}" name="{@name}"
          xsl:if="contains(@attrs, 'readonly')"> readonly="readonly"</xsl:if>/>
  </xsl:template>

</xsl:stylesheet>